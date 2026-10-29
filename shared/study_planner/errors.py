class StudyPlannerError(Exception):
    pass


class InfeasiblePlan(StudyPlannerError):
    def __init__(self, needed_h: float, available_h: float):
        self.needed_h = needed_h
        self.available_h = available_h
        super().__init__(
            f"Infeasible plan: Requires {needed_h:.1f}h, but only {available_h:.1f}h are available."
        )
