from app import db


class Goal(db.Model):
    goal_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    tasks = db.relationship("Task", back_populates="goal", lazy=True)

    def to_dict(self):
        return dict(
            id=self.goal_id,
            title=self.title
        )

    @classmethod
    def from_dict(cls, goal_data):
        new_goal = Goal(title=goal_data["title"])
        return new_goal
    

# _______________ 
# |             |
# |    Thank    |
# |   you for   |
# |  reviewing  |
# |   my code!  | 
# |_____________|  
#       || 
# (\__/ || 
# (•ㅅ•) || 
# / 　 >||