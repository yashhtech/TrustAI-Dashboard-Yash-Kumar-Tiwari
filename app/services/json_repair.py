import json


class JSONRepair:

    @staticmethod
    def repair(content):

        try:
            return json.loads(content)

        except Exception:

            try:

                start = content.find("{")
                end = content.rfind("}")

                if start == -1 or end == -1:
                    raise Exception()

                cleaned = content[start:end + 1]

                return json.loads(cleaned)

            except Exception:

                return None