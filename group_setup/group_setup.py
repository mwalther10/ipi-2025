import os
from dotenv import load_dotenv
import requests


def create_new_group(
    group_name: str,
    course_id: str,
    cookie_moodle_session: str,
    parameter_sesskey: str,
) -> int:
    cookies = {
        "MoodleSession": cookie_moodle_session,
    }

    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "no-cache",
        "content-type": "application/x-www-form-urlencoded",
        "origin": "https://moodle.uni-heidelberg.de",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": f"https://moodle.uni-heidelberg.de/group/group.php?courseid={course_id}",
        "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    }

    data = {
        "id": "",
        "courseid": course_id,
        "sesskey": parameter_sesskey,
        "_qf__group_form": "1",
        "mform_isexpanded_id_general": "1",
        "name": group_name,
        "idnumber": "",
        "enrolmentkey": "",
        "visibility": "0",
        "participation": [
            "0",
            "1",
        ],
        "enablemessaging": "0",
    }

    response = requests.post(
        "https://moodle.uni-heidelberg.de/group/group.php",
        cookies=cookies,
        headers=headers,
        data=data,
    )

    return response.status_code


if __name__ == "__main__":
    load_dotenv()

    tutors = os.environ["TUTOR_NAMES"].split(";")
    groups_per_tutor = int(os.environ["GROUPS_PER_TUTOR"])

    print(tutors)

    group_number = 1
    for tutor in tutors:
        for i in range(groups_per_tutor):
            group_name = f"{group_number:03}_{tutor}"
            status_code = create_new_group(
                group_name=group_name,
                course_id=os.environ["COURSE_ID"],
                cookie_moodle_session=os.environ["COOKIE_MoodleSession"],
                parameter_sesskey=os.environ["PARAMETER_sesskey"],
            )
            print(f"Created group '{group_name}' with status code: {status_code}")
            group_number += 1
