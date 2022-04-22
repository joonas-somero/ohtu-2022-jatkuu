from matchers import All, And, Or, PlaysIn, HasAtLeast, HasFewerThan

class QueryBuilder:
    def __init__(self, matcher=All()):
        self._matcher_object = matcher

    def build(self):
        return self._matcher_object

    def playsIn(self, team):
        return QueryBuilder(
            And(self._matcher_object, PlaysIn(team))
        )
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(
            And(self._matcher_object, HasAtLeast(value, attr))
        )

    def hasFewerThan(self, value, attr):
        return QueryBuilder(
            And(self._matcher_object, HasFewerThan(value, attr))
        )

    def oneOf(self, *queries):
        return QueryBuilder(
            Or(*queries)
        )
