class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        secret_knowledge_set = set([0, firstPerson])

        sorted_meetings_list = []
        meetings.sort(key=lambda x: x[2])

        seen_time_set = set()

        for meet in meetings:
            if meet[2] not in seen_time_set:
                seen_time_set.add(meet[2])
                sorted_meetings_list.append([])
            sorted_meetings_list[-1].append((meet[0], meet[1]))

        for meeting_group in sorted_meetings_list:
            people_know_secret_set = set()
            adjacency_graph = defaultdict(list)

            for person1, person2 in meeting_group:
                adjacency_graph[person1].append(person2)
                adjacency_graph[person2].append(person1)
                if person1 in secret_knowledge_set:
                    people_know_secret_set.add(person1)
                if person2 in secret_knowledge_set:
                    people_know_secret_set.add(person2)

            people_queue = deque(people_know_secret_set)

            while people_queue:
                current_person = people_queue.popleft()
                secret_knowledge_set.add(current_person)
                for neighbor in adjacency_graph[current_person]:
                    if neighbor not in secret_knowledge_set:
                        secret_knowledge_set.add(neighbor)
                        people_queue.append(neighbor)

        return list(secret_knowledge_set)
