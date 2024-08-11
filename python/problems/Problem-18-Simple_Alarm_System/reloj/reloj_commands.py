from reloj.reloj import Reloj


class GetCurrentTimeCommand:
    """Get current time in H:M:S format.
    """
    @staticmethod
    def execute():
        Reloj.get_current_time()
    

class DisplayAlarmsCommand:
    """Display active alamrs
    """
    @staticmethod
    def execute():
        Reloj.display_alarms()
    

class CreateNewAlarmCommand:
    """Creates new alarm
    """
    @staticmethod
    def execute(data: dict = {}):
        assert isinstance(data, dict), f"data: {data} must be a dictionary!"

        if not data:
            return Reloj()
        
        Reloj().create_new_alarm(**data)

        return "New alarm added!"
    

class EditAlarmCommand:
    """Edits existing alarm
    """
    @staticmethod
    def execute(data: dict = {}):
        assert isinstance(data, dict), f"data: {data} must be a dictionary!"

        if not data:
            return False
        
        if 'id' not in data.keys():
            raise ValueError("id must be present in data")
        
        id = data['id']
        if id < 0:
            raise ValueError("id must be an integer grater than zero!")
        
        if not len(Reloj.instances):
            raise ValueError("There is no alarms!")
        
        if id > len(Reloj.instances):
            raise ValueError("the id number is not in reloj instances")
        
        alarm = Reloj.get_alarm_by_id(id)

        if alarm:
            if 'horas' in data.keys():
                alarm.agregar_horas(data['horas'])

            if 'minutos' in data.keys():
                alarm.agregar_minutos(data['minutos'])

            if 'segundos' in data.keys():
                alarm.agregar_segundos(data['segundos'])

            return "The alarm has been edited"


class DeleteAlarmCommand:
    """Deletes an alarm
    """
    @staticmethod
    def execute(id: int):
        assert isinstance(id, int), f"id: {id} must be an integer!"
        assert len(Reloj.instances), f'There is no alarms!'
        assert id < len(Reloj.instances), f"the id number is not in reloj instances"
        assert id >= 0, f"id must be an integer grater or equal than zero!"
        
        Reloj.delete_alarm(id)

        return "The alarm has been deleted"

