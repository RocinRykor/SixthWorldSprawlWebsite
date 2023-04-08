from typing import Dict

from sixthworldsprawl.utils.constants import matrix_constants as Matrix
from sixthworldsprawl.utils.rollers import dice_roller


def generate_sheaf(host_level: int, security_rating: int, has_nasty_surprises: bool) -> None:
    alert_level_table: Dict[int, str] = {
        0: Matrix.NO_ALERT,
        1: Matrix.PASSIVE_ALERT,
        2: Matrix.ACTIVE_ALERT,
        3: Matrix.SHUTDOWN
    }

    alert_level = 0  # 0 = No Alert, 1 = Passive, 2 = Active, 3 = Shutdown
    steps_since_last_alert = 0
    while alert_level < 3:  # Has not yet reached Alert Level: Shutdown
        # Step 1: Trigger Step
        current_step += roll_trigger_step(host_level)  # Increment Step Counter
        sheaf_step = SheafStep(current_step)  # Generate a new Sheaf Step

        # Step 2: Alert Level

        # alertContainer = roll_alert_table(alert_level, steps_since_last_alert, False)
        # generate_ic = True

        # if alertContainer.is_alert_step:
        #     steps_since_last_alert = 0
        #     alert_level += 1

        #     print(f"{current_step} -> Alert Status: {alert_level_table[alert_level]}")

        #     sheaf_step.set_title(alert_level_table[alert_level])

        #     if host_level <= 1 or alert_level == 3:
        #         generate_ic = False
        #     else:
        #         alertContainer = roll_alert_table(alert_level, steps_since_last_alert, True)
        # else:
        #     steps_since_last_alert += 1

        # if generate_ic:
        #     sheaf_step.addIC(ProcessIC(alertContainer, current_step))

        # print(f"{current_step}: {sheaf_step.listIC()}")


def roll_trigger_step(host_level: int) -> int:
    base_step = sum(dice_roller.roll(1, 3))

    switch = {
        0: base_step + 4,
        1: base_step + 3,
        2: base_step + 2,
        3: base_step + 1
    }
    return switch.get(host_level, "Invalid Number")


def roll_alert_table(alert_level: int, steps_since_last_alert: int, limit_to_ic: bool) -> AlertContainer:
    roll_result = sum(dice_roller.roll(1, 6))

    final_results = roll_result if limit_to_ic else roll_result + steps_since_last_alert

    if alert_level == 0:
        if finalResult in [1, 2, 3]:
            return AlertContainer(Matrix.WHITE, Matrix.REACTIVE)
        elif finalResult in [4, 5]:
            return AlertContainer(Matrix.WHITE, Matrix.PROACTIVE)
        elif finalResult in [6, 7]:
            return AlertContainer(Matrix.GRAY, Matrix.REACTIVE)
        else:
            return AlertContainer()
    elif alert_level == 1:
        if finalResult in [1, 2, 3]:
            return AlertContainer(Matrix.WHITE, Matrix.PROACTIVE)
        elif finalResult in [4, 5]:
            return AlertContainer(Matrix.GRAY, Matrix.REACTIVE)
        elif finalResult in [6, 7]:
            return AlertContainer(Matrix.GRAY, Matrix.PROACTIVE)
        else:
            return AlertContainer()
    else:
        if finalResult in [1, 2, 3]:
            return AlertContainer(Matrix.GRAY, Matrix.PROACTIVE)
        elif finalResult in [4, 5]:
            return AlertContainer(Matrix.WHITE, Matrix.PROACTIVE)
        elif finalResult in [6, 7]:
            return AlertContainer(Matrix.BLACK, None)
        else:
            return AlertContainer()


class SheafStep:
    def __init__(self, current_step):
        self.current_step = current_step
        self.title = ""
        self.ic_list = []
        self.is_construct = False
        self.is_party_cluster = False

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def add_ic(self, ic_program):
        self.ic_list.append(ic_program)

    def is_construct(self):
        return self.is_construct

    def set_construct(self, is_construct):
        self.is_construct = is_construct

    def is_party_cluster(self):
        return self.is_party_cluster

    def set_party_cluster(self, is_party_cluster):
        self.is_party_cluster = is_party_cluster

    def get_ic_list(self):
        return self.ic_list

    def list_ic(self):
        if len(self.ic_list) == 0:
            return ""
        elif len(self.ic_list) == 1:
            return str(self.ic_list[0])
        else:
            return str(self.ic_list)


class AlertContainer:
    def __init__(self, level_ic=None, category_ic=None):
        self.level_ic = level_ic
        self.category_ic = category_ic

    def get_level_ic(self):
        return self.level_ic

    def get_category_ic(self):
        return self.category_ic

    current_step = 0
