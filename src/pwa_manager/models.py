from dataclasses import dataclass
from pathlib import Path


@dataclass
class PWAApplication:

    name: str
    desktop_file: Path
    icon: str | None = None
    source: str = "unknown"
    app_type: str = "unknown"


    @property
    def normalized_name(self):

        name = self.name.lower().strip()

        replacements = {
            ": ваш помічник із ші": "",
            "otwórz kalendarz": "outlook",
            "open calendar": "outlook",
        }

        for old, new in replacements.items():
            name = name.replace(
                old,
                new
            )

        return name.strip()


    @property
    def display_name(self):

        names = {

            "microsoft copilot":
                "Microsoft Copilot",

            "google gemini":
                "Google Gemini",

            "microsoft word":
                "Microsoft Word",

            "microsoft excel":
                "Microsoft Excel",

            "microsoft powerpoint":
                "Microsoft PowerPoint",

            "outlook":
                "Outlook",

        }

        return names.get(
            self.normalized_name,
            self.name
        )
