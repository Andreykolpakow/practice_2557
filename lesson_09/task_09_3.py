# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
# с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    position_wages = {
        'director': {'wage': 1500, 'bonus': 1000},
        'manager': {'wage': 500, 'bonus': 1500},
        'secretary': {'wage': 500, 'bonus': 100},
        'assistant_director': {'wage': 700, 'bonus': 700},
        'security_guard': {'wage': 300, 'bonus': 100}
    }
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = self.position_wages.get(self.position)


class Position(Worker):
    # def __init__(self, name, surname, position):
    #     super().__init__(name, surname, position)
    def get_full_name(self):
        return (f'{self.name} {self.surname}')

    def get_total_income(self):
        # total_income = self._income['wage'] + self._income['bonus']
        return (f"total income {self._income['wage'] + self._income['bonus']} $")

ivanov = Position('Ivan', 'Ivanov', 'manager')
petrov = Position('Petr', 'Petrov', 'director')
sidorova = Position('Anna', 'Sidorova', 'secretary')
ivanov.get_full_name
print(f'Работнику {ivanov.get_full_name()} на должности {ivanov.position} по штатному расписанию положен '
      f'оклад {ivanov._income["wage"]}$ и премия при выполнени должностных инструкций в размере '
      f'{ivanov._income["bonus"]}$. Итого ФОТ работника может достигать: {ivanov.get_total_income()}')
print(f'Работнику {petrov.get_full_name()} на должности {petrov.position} по штатному расписанию положен '
      f'оклад {petrov._income["wage"]}$ и премия при выполнени должностных инструкций в размере '
      f'{petrov._income["bonus"]}$. Итого ФОТ работника может достигать: {petrov.get_total_income()}')
print(f'Работнику {sidorova.get_full_name()} на должности {sidorova.position} по штатному расписанию положен '
      f'оклад {sidorova._income["wage"]}$ и премия при выполнени должностных инструкций в размере '
      f'{sidorova._income["bonus"]}$. Итого ФОТ работника может достигать: {sidorova.get_total_income()}')