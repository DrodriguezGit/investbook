from __future__ import annotations
from typing import Union
from nicegui import ui
from nicegui.binding import BindableProperty

from webapp.front.components.table.elements import (
    Row,
    Column,
    EditableNumberColumn,
    ChipColumn,
    SelectColumn,
    ToggleColumn,
    DeleteColumn
)



class Table(ui.table):
    # TODO: revisar comportamiento del update
    nchanged: int = BindableProperty()
    nupdated: int = BindableProperty()
    ncreated: int = BindableProperty()
    ndeleted: int = BindableProperty()

    def __init__(
            self,
            cols: list[Union[Column, EditableNumberColumn, ChipColumn, SelectColumn, ToggleColumn, DeleteColumn]],
            init_data: list[dict] | None=None,
            csv_cols: list=None,
            table_classes: str | None=None,
            table_props: str | None=None,
            header_style: str | None=None,
            columns_style: dict | None=None,
            pagination: int=10
        ) -> None:

        self.header_style = header_style
        self.cols = cols
        self.csv_cols = csv_cols or [col.name for col in cols]
        self._instances = [self.row_instance(values, status='persisted') for values in init_data]
        init_rows = [row.data for row in self._instances]

        super().__init__(
            rows=init_rows,
            columns=self.column_definition,
            column_defaults=columns_style,
            pagination=pagination
        )

        self.classes(table_classes)
        self.props(table_props)

        for col in cols:

            if isinstance(col, DeleteColumn):

                self.add_slot(f'body-cell-{col.name}', col.template)
                self.on(col.name, lambda id: self.row_delete(id.args))

            if isinstance(col, (EditableNumberColumn, SelectColumn)):

                self.add_slot(f'body-cell-{col.name}', col.template)
                self.on(col.name, lambda e: self.row_update(e.args['id'], e.args))

            if isinstance(col, ToggleColumn):

                for row in self._instances:
                    row.values[col.name] = col.checked
                    row.data[col.name] = col.checked

                self.add_slot(f'body-cell-{col.name}', col.template)
                self.on(col.name, lambda e: self.row_update(e.args['id'], e.args))

            if isinstance(col, ChipColumn):

                self.add_slot(f'body-cell-{col.name}', col.template)

    @property
    def column_definition(self):
        return [
            {
                'name': column.name,
                'label': column.label,
                'field': column.name,
                'headerStyle': column.header_styles or self.header_style,
                'sortable': column.sortable
            } for column in self.cols
        ]
    
    @property
    def model(self) -> list[Row]:
        return self._instances
    
    @property
    def nchanged(self):
        return self.nupdated + self.ncreated + self.ndeleted
    
    @property
    def updated(self):
        return [i for i in self.model if i.status == 'updated']
    
    @property
    def nupdated(self):
        return len(self.updated)
    
    @property
    def created(self):
        return [i for i in self.model if i.status == 'created']
    
    @property
    def ncreated(self):
        return len(self.created)
    
    @property
    def deleted(self):
        return [i for i in self.model if i.status == 'deleted']
    
    @property
    def ndeleted(self):
        return len(self.deleted)
    
    def persist(self):
        for row in self._instances:
            row.status = 'persisted'
    
    def row_instance(self, values: dict, status: str):
        return Row(values=values, status=status)
    
    def row_delete(self, id):

        instance = next((x for x in self._instances if x.id == id), None)

        if instance.status == 'created':
            instance.status = 'temporal'
        else:
            instance.status = 'deleted'

        self.rows[:] = [row for row in self.rows if row[self.row_key] != id]

        self.update()
    
    def row_create(self, values: dict):

        instance = self.row_instance(values, status='created')

        self._instances.append(instance)

        self.rows.extend([instance.data])

        self.update()

    def row_update(self, id: int, values: dict):

        instance = next((x for x in self._instances if x.id == id), None)

        instance.data.update(**values)

        current_data = instance.data.copy()

        current_data.pop('id')

        if instance.status == 'created':
            pass
        elif instance.status == 'updated':
            if current_data == instance.values:
                instance.status = 'temporal'
        else:
            instance.status = 'updated'