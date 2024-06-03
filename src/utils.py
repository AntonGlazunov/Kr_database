def emp_info(vacancies_list):
    unique_employers = []
    emp_list_info = []
    for vacancy in vacancies_list:
        if vacancy["employer"] not in unique_employers:
            unique_employers.append(vacancy["employer"])
    for employer in unique_employers:
        emp_list_info.append(f"({employer["id"]}, '{employer["name"]}', '{employer["url"]}')")
    return emp_list_info


def vacancy_info(vacancies_list):
    vacancies_list_info = []
    for vacancy in vacancies_list:
        if vacancy["salary"] is None:
            vacancy["salary"] = {"from": 0, "to": 0, "currency": "RUR"}
        if vacancy["salary"].get("from") is None:
            vacancy["salary"] = {"from": 0, "to": vacancy["salary"]["to"],
                                 "currency": vacancy["salary"]["currency"]}
        if vacancy["salary"].get("to") is None:
            vacancy["salary"] = {"from": vacancy["salary"]["from"], "to": 0,
                                 "currency": vacancy["salary"]["currency"]}
        vacancies_list_info.append(f"({vacancy["id"]}, '{vacancy["name"]}', '{vacancy["area"]["name"]}', "
                                   f"{vacancy["salary"]["from"]}, {vacancy["salary"]["to"]}, "
                                   f"'{vacancy["salary"]["currency"]}', '{vacancy["published_at"]}', "
                                   f"'{vacancy["alternate_url"]}', "
                                   f"'{str(vacancy["snippet"]["requirement"]).replace("'", " ")}', "
                                   f"'{str(vacancy["snippet"]["responsibility"]).replace("'", " ")}', "
                                   f"{vacancy["employer"]["id"]})")
    return vacancies_list_info
