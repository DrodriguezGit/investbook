from __future__ import annotations
from dataclasses import dataclass, field


@dataclass
class Row:
    values: dict
    id: int = field(init=False)
    status: str = 'persisted' # 'persisted' | 'created' | 'updated' | 'deleted' | 'temporal'
    data: dict = field(init=False)

    def __post_init__(self):
        self.id = id(self)
        self.data = dict(self.values, id=self.id)


@dataclass
class Column:
    name: str
    label: str = None
    sortable: bool = True
    header_styles: str = None


@dataclass
class DeleteColumn(Column):
    icon: str = 'delete'
    color: str = 'red'
    styles: str = ''

    @property
    def template(self):
        return f'''
            <q-td key="{self.name}" :props="props">
                <q-btn
                    @click="() => $parent.$emit('{self.name}', props.row.id)"
                    icon="{self.icon}"
                    color="{self.color}"
                    {self.styles}
                />
            </q-td>
        '''


@dataclass
class EditableNumberColumn(Column):
    precision: float = 1
    step: float = 1
    styles: str = ''

    @property
    def template(self):
        return f'''
            <q-td key="{self.name}" :props="props">
                <div class="q-gutter-none flex items-center justify-center">
                    <q-input
                        v-model="props.row.{self.name}"
                        type="number"
                        step="{self.step}"
                        @blur="props.row.{self.name} = parseFloat(props.row.{self.name}).toFixed({self.precision})"
                        @update:model-value="() => $parent.$emit('{self.name}', {{ id: props.row.id,  {self.name}: parseFloat(props.row.{self.name}) }})"
                        {self.styles}
                    />
                </div>
            </q-td>
        '''


@dataclass
class ChipColumn(Column):
    field_color: str = ''
    field_label: str = ''
    style: str = ''

    @property
    def template(self):
        return f'''
            <q-td key="{self.name}" :props="props">
                <div class="q-gutter-none flex items-center justify-center">
                    <q-chip
                        :color="props.row.{self.field_color}"
                        text-color="white"
                        :label="props.row.{self.field_label}"
                        style="{self.style}"
                    />
                </div>
            </q-td>
        '''

@dataclass
class SelectColumn(Column):
    options: list = field(default_factory=list)


    @property
    def template(self):
        return f'''
            <q-td key="{self.name}" :props="props">
                <q-select
                    v-model="props.row.{self.name}"  
                    :options="{str(self.options)}"
                    @update:model-value="() => $parent.$emit('{self.name}', {{ id: props.row.id, {self.name}: props.row.{self.name} }})"
                    dense borderless
                />
            </q-td>
        '''

@dataclass
class ToggleColumn(Column):
    checked: bool=True

    @property
    def template(self):
        return f'''
            <q-td key="{self.name}" :props="props">
                <div class="q-gutter-none flex items-center justify-center">
                    <q-toggle
                        v-model="props.row.{self.name}"
                        @update:model-value="() => $parent.$emit('{self.name}', {{ id: props.row.id, {self.name}: props.row.{self.name} }})"
                    />
                </div>
            </q-td>
        '''