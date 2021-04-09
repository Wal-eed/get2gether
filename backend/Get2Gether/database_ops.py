"""
A suite of database operations that abstract over the specific DBMS used and the driver
library or ODM used to interface with that DBMS.
"""
import re
from Get2Gether.utils.colourisation import printColoured
from Get2Gether.utils.debug import pretty
from Get2Gether.exceptions import InvalidUserInput
from typing import (
    Dict, 
    List,
    Callable
)
import json
from bson import ObjectId

# ============================================ START =====================================================


# Our database functions go here

def save_schedule(schedule, filename):
    """

    """
    # Save to filename

















# ========================================================================================================

# class JSONEncoder(json.JSONEncoder):
#     """
#         Given a document retrieved from the database, returns a JSON
#         serialisable version.
#             Eg.
#                 results = db.sample.find() 
#                 json_compatible_results = JSONEncoder().encode(results)
#     """
#     def default(self, o):
#         if isinstance(o, ObjectId):
#             return str(o)
#         return json.JSONEncoder.default(self, o)


# def insert(collection_name: str, document: Dict) -> str:
#     """ 
#         Inserts and returns the ID of the newly inserted document in the target collection 

#         Args:
#             collection_name (str) 
#             document (dict)

#         Returns:
#             str: ID of the newly inserted item
#     """
#     print(" ➤ Inserting: {}, in {}".format(document, collection_name))
#     insertion_result = db[collection_name].insert_one(document)
#     return str(insertion_result.inserted_id)

# # ===== Courses Operations =====

# def get_courses_lessons() -> List:
#     """
#         Retrieves all courses from the current database instance.   # TODO clarify the different between this and the function below

#         Returns:
#             list: all courses and their associated lesson details
#     """
#     courses = db.courses_lessons.find_one()
#     courses["_id"] = str(courses["_id"])
#     return courses

# def get_courses_all() -> List:
#     """
#         Retrieves all courses from the current database instance.

#         Returns:
#             list: all courses and their associated lesson details
#     """
#     courses = [ course for course in db.courses_all.find() ]
#     for each_course in courses:
#         each_course["_id"] = str(each_course["_id"])
#     return courses

# def get_courses_full():
#     """
#         Retrieves all courses with MAXIMAL AMOUNT OF DETAIL
#     """
#     courses = [ course for course in db.courses_full.find() ]
#     for each_course in courses:
#         each_course["_id"] = str(each_course["_id"])
#     return courses

# # ===== Lessons Operations =====

# def get_all_lessons(course_id: str) -> List:
#     """
#         TODO: documentation
#     """
#     try:
#         course = db.courses_full.find_one({ "courseId": course_id })
#         # for each_lesson in course["lessons"]:
#         #     each_lesson["_id"] = str(each_lesson["_id"])
#         return course["lessons"]
#     except:
#         raise InvalidUserInput(
#             description="Failed to find the course '{}'".format(
#                 course_id
#             )
#         )

# def get_lesson(course_id: str, lesson_id: str) -> List:
#     """
#         Retrieves the lesson with the target lesson_id

#         Args:
#             course_id (str)
#             lesson_id (str)
        
#         Returns:
#             dict: mapped from the 'lesson' json document
#     """
#     try:
#         course = db.courses_full.find_one({ "courseId": course_id })
#         lesson = [ l for l in course["lessons"] if l["lessonId"] == lesson_id ][0]
#         lesson["_id"] = str(lesson["_id"])
#         return lesson
#     except:
#         raise InvalidUserInput(
#             description="Failed to find: course '{}', lesson '{}'".format(
#                 course_id, lesson_id
#             )
#         )

# # TODO: stub function for getting the lesson difficulty:
# def determine_lesson_difficulty(course_id: str, lesson_id: str):
#     """

#     """
#     p = re.compile("\w+-(\d+)")
#     result = p.search(lesson_id)
#     return int(result.group(1)) * 500

# def get_lesson_difficulty(course_id: str, lesson_id: str):
#     try: 
#         # target_course = [ course for course in all_course if course["courseId"] == course_id ][0] 
#         # target_lesson = [ lesson for lesson in target_course["lessons"] ]
#         difficulty = determine_lesson_difficulty(course_id, lesson_id)
#         printColoured(" ➤ Found '{}' lesson '{}' of difficulty: {}".format(course_id, lesson_id, difficulty))
#         return difficulty
#     except Exception as err:
#         print("HERE: {}".format(err))
#         raise InvalidUserInput(
#             description="Failed to find course '{}', lesson '{}'".format(
#                 course_id, lesson_id
#             )
#         )

# # ===== Children Management =====

# def save_child(child, parent_user_id):
#     """
#         TODO
#         multiple children with the same name unsupported
#     """
#     parent = get_user(user_id=parent_user_id)
#     new_children = parent["children"].copy()
#     child["_id"] = "{}-{}".format(parent_user_id, child["name"])
#     child["statistics"] = []
#     child["most_recent_course_id"] = ""
    
#     # Default recommendation engine parameters
#     child["rec_params"] = {
#         "k_factor": 95,
#         "incorrect_penalty_factor": 10,
#         "expected_time": 40,
#         "time_multiplier": 0.05
#     }
#     new_children.append(child)
#     db.users.update_one({ "_id": ObjectId(parent_user_id) }, { "$set": { "children": new_children } })
#     return (get_user(user_id=parent_user_id), child["_id"])

# # ===== Statistics Operations =====

# def get_stats(parent_user_id: str, child_id: str):
#     """
#         TODO
#     """
#     parent = get_user(user_id=parent_user_id)
#     target_child = [ child for child in parent["children"] if child["_id"] == child_id ][0]

#     stats = target_child["statistics"]
#     categorical_stats = {
#         "shapes": [ stat for stat in stats if stat["course_id"] == "shapes" ],
#         "emotions": [ stat for stat in stats if stat["course_id"] == "emotion" ],
#         "actions": [ stat for stat in stats if stat["course_id"] == "actions" ],
#         "colours": [ stat for stat in stats if stat["course_id"] == "colours" ],
#         "objects": [ stat for stat in stats if stat["course_id"] == "objects" ]
#     }
#     curr_proficiencies = target_child["proficiency"]
#     return {
#         "proficiencies": curr_proficiencies,
#         "categorical_stats": categorical_stats
#     }

# def clear_child_stats(parent_user_id: str, child_id: str):
#     """
#         TODO this is just a convenience function
#     """
#     try:
#         db.users.update_one(
#             {
#                 "_id": ObjectId(parent_user_id),
#                 "children": {
#                     "$elemMatch": {
#                         "_id": {
#                             "$eq": child_id
#                         }
#                     }
#                 }
#             },
#             {
#                 "$set": {
#                     "children.$.statistics": []
#                 }
#             }
#         )
#     except:
#         raise InvalidUserInput(description="Failed to clear")

# def save_stats(stats, parent_user_id, child_id):
#     """
#         TODO
#         pushes an object to db.users.children.statistics array
#         ALSO saves the most_recent_course_id
#     """
#     parent = get_user(user_id=parent_user_id)
#     target_child = [ child for child in parent["children"] if child["_id"] == child_id ][0]
#     # new_stats = target_child["statistics"].copy()
#     # new_stats.append(stats)
#     most_recent_course_id = stats["course_id"]

#     # TODO: it's suboptimal to update twice. Haven't figured out how to merge the two actions 
#     db.users.update_one(
#         {
#             "_id": ObjectId(parent_user_id),
#             "children": {
#                 "$elemMatch": {
#                     "_id": {
#                         "$eq": child_id
#                     }
#                 }
#             }
#         },
#         {
#             "$push": {
#                 "children.$.statistics": stats
#             }
#         }
#     )
#     db.users.update_one(
#         {
#             "_id": ObjectId(parent_user_id),
#             "children": {
#                 "$elemMatch": {
#                     "_id": {
#                         "$eq": child_id
#                     }
#                 }
#             }
#         },
#         {
#             "$set": {
#                 "children.$.most_recent_course_id": most_recent_course_id
#             }
#         }
#     )
#     printColoured(" ➤ Successfully saved new performance stats!")
#     return stats

# def get_stats_in_range(parent_user_id: str, child_id: str, course_id: str, start_timestamp: int, end_timestamp: int):
#     """
#         Given a parent user_id and child_id, finds that child and extracts their performance
#         statistics 
#     """
#     parent = get_user(user_id=parent_user_id)
#     target_child = [ child for child in parent["children"] if child["_id"] == child_id ][0]
#     all_stats = [ 
#         stat for stat in target_child["statistics"] 
#         if (
#             start_timestamp <= int(stat["time_on_completion"]) <= end_timestamp
#         ) and (
#             stat["course_id"] == course_id
#         )
#     ] 
#     return all_stats

# # ===== User Operations =====

# def get_all_users() -> List[Dict]:
#     """
#         Fetches all users from the database

#         Returns:
#             list: all users in the 'users' collection of the database instance
#     """
#     return [ user for user in db.users.find() ]

# def save_user(user) -> str:
#     """ 
#         Saves and returns the ID of the new user 

#         Returns:
#             str: ID of the new user
#     """
#     printColoured(" ➤ Saving new user: {}".format(user), colour="blue")
#     # Builtin function vars() takes an object and constructs a dict. The _id key is then
#     # removed to prevent colliding with MongoDB's generated ID
#     document = vars(user)
#     del document["_id"]
#     return insert("users", document)

# def wipe_all_users():
#     """ Wipes all documents from the Get2Gether 'users' collection """
#     db.users.drop()
#     printColoured(" ➤ DROPPED USERS", colour="red")

# def get_user(user_id: str) -> Dict: 
#     """ 
#         Fetches the user with the given ID (the one that's assigned by MongoDB
#         under the hood)

#         Args:
#             user_id (str)
        
#         Returns:
#             dict: of shape: { _id, name, email, password }
#     """
#     try:
#         target_user = db.users.find_one({"_id": ObjectId(user_id)})
#         target_user["_id"] = str(target_user["_id"])
#         return target_user
#     except:
#         raise InvalidUserInput(description="Failed to find user with id: {}".format(user_id))

# def get_user_by_email(email):
#     """
#         Fetches the user by email rather than user_id

#         Args:
#             email (str)

#         Returns:
#             dict: of shape: { _id, name, email, password }
#     """
#     target_user = db.users.find_one({"email": email})
#     if target_user == None:
#         return None
#     details = {
#         "_id": str(target_user["_id"]),
#         "name": target_user["name"],
#         "email": target_user["email"],
#         "password": target_user["password"],
#         "children": target_user["children"]
#     }
#     return details

# def get_child_proficiency(user_id: str, child_id: str, course_id: str):
#     """
#         TODO: 
#         Given the target user and child, gets that child's current
#         proficiency rating for a given category
#     """
#     printColoured(" > Getting proficiency for {} in course: {}".format(child_id, course_id), colour="yellow")
#     parent = get_user(user_id)
#     child = [ child for child in parent["children"] if child["_id"] == child_id ][0]
#     return int(child["proficiency"][course_id])

# def set_child_proficiency(parent_user_id: str, child_id: str, course_id: str, new_proficiency: int):
#     parent = get_user(parent_user_id)
#     child = [ child for child in parent["children"] if child["_id"] == child_id ][0]

#     db.users.update_one(
#         {
#             "_id": ObjectId(parent_user_id),
#             "children": {
#                 "$elemMatch": {
#                     "_id": {
#                         "$eq": child_id
#                     }
#                 }
#             }
#         },
#         {
#             "$set": {
#                 "children.$.proficiency.{}".format(course_id): new_proficiency
#             }
#         }
#     )
#     print(" @@@@@@@@@@@@@@@@@@@@@@@@@")

# def password_verified(email, password):
#     """
#         Given an email and password, verifies it against the
#         hashed password stored in the database 
#     """
#     user = get_user_by_email(email)
#     if user == None:
#         return False
#     # TODO: need to hash passwords
#     return user["password"] == password

# def email_taken(email):
#     return db.users.find_one({ "email": email })


# def wipe_user(email):
#     """
#         TODO unprotected! This is just a convenience function
#     """
#     printColoured(" ➤ Removing a user: {}".format(email), colour="yellow")
#     db.users.remove({"email": email})

# def get_rec_params(parent_user_id: str, child_id: str):
#     """
#         TODO: gets the child's rec engine parameters
#     """
#     # Fetch child from db and return their parameters
#     parent = get_user(parent_user_id)
#     child = [ child for child in parent["children"] if child["_id"] == child_id ][0]
#     return child["rec_params"]

# def set_rec_params(
#         parent_user_id: str, 
#         child_id: str, 
#         exp_time: int, 
#         incorrect_penalty_factor: float, 
#         time_multiplier: float,
#         k_factor: float
#     ):
#     """
#         TODO: sets the child's rec engine parameters
#     """
#     parent = get_user(parent_user_id)
#     child = [ child for child in parent["children"] if child["_id"] == child_id ][0]
#     db.users.update_one(
#         {
#             "_id": ObjectId(parent_user_id),
#             "children": {
#                 "$elemMatch": {
#                     "_id": {
#                         "$eq": child_id
#                     }
#                 }
#             }
#         },
#         {
#             "$set": {
#                 "children.$.rec_params": {
#                     "exp_time": exp_time, 
#                     "incorrect_penalty_factor": incorrect_penalty_factor, 
#                     "time_multiplier": time_multiplier,
#                     "k_factor": k_factor
#                 }
#             }
#         }
#     )
#     return {
#         "new_params": {
#             "exp_time": exp_time, 
#             "incorrect_penalty_factor": incorrect_penalty_factor, 
#             "time_multiplier": time_multiplier,
#             "k_factor": k_factor
#         }
#     }
