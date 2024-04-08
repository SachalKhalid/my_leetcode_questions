class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # Count the number of students preferring each type of sandwich
        preferences = [0, 0]  # Index 0 for circular sandwiches, index 1 for square sandwiches
        for preference in students:
            preferences[preference] += 1
        
        # Iterate through sandwiches
        for sandwich in sandwiches:
            # If there are no more students left who prefer this type of sandwich, return the count
            if preferences[sandwich] == 0:
                return sum(preferences)
            
            # Serve the student if their preferred sandwich matches the current one
            preferences[sandwich] -= 1
        
        # If the loop completes without returning, it means all students got their sandwiches
        return 0