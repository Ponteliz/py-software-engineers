from app.developers.backend_developer import BackendDeveloper
from app.developers.frontend_developer import FrontendDeveloper


class FullStackDeveloper(BackendDeveloper, FrontendDeveloper):

    def __init__(self, name: str) -> None:
        super().__init__(name)

        for skill in ["JavaScript", "HTML", "CSS"]:
            if skill not in self.skills:
                self.skills.append(skill)

    def create_web_application(self) -> None:
        print(f"{self.name} started creating a web application...")
        self.create_powerful_api()
        self.create_awesome_web_page()
