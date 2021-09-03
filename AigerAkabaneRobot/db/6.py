from pymongo import DeleteOne

from AigerAkabaneRobot.services.mongo import mongodb
from AigerAkabaneRobot.utils.logger import log

log.info("Aiger Akabane Database v6")
log.info("Feds: fix str user_id and fix duplications")
log.info("Starting updating all feds...")

queue = []

all_bans = mongodb.fed_bans.find({"user_id": {"$type": "string"}})
all_bans_count = all_bans.count()
counter = 0
changed_feds = 0

for ban in all_bans:
    counter += 1
    changed_feds += 1
    queue.append(DeleteOne({"_id": ban["_id"]}))

mongodb.fed_bans.bulk_write(queue)

log.info("Update done!")
log.info("Modified feds - " + str(changed_feds))
