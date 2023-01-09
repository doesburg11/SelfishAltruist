from typing import Type, Callable
from collections import defaultdict

import mesa


class BaseSchedulerByFilteredType(mesa.time.BaseScheduler):

    def __init__(self, model: mesa.Model) -> None:
        super().__init__(model)
        self.agents_by_type = defaultdict(dict)

    def add(self, agent: mesa.Agent) -> None:
        """
        Add an Agent object to the schedule

        Args:
            agent: An Agent to be added to the schedule.
        """
        super().add(agent)
        agent_class: type[mesa.Agent] = type(agent)
        self.agents_by_type[agent_class][agent.unique_id] = agent

    def get_type_count(
            self,
            type_class: Type[mesa.Agent],
            filter_func: Callable[[mesa.Agent], bool] = None,
    ) -> int:
        """
        Returns the current number of agents of certain type in the queue that satisfy the filter function.
        """
        count = 0
        for agent in self.agents_by_type[type_class].values():
            if filter_func is None or filter_func(agent):
                count += 1
        return count

