class Member:
    def __init__(self, name):
        self.name = name

    def book_session(self, session_name, *extras, **details):
        print(f"Booking {session_name} for {self.name}")
        print(extras)
        print(details)


class VIPMember(Member):
    def __init__(self, name, vip_level):
        super().__init__(name)
        self.vip_level = vip_level

    def book_session(self, session_name, *extras, **details):
        print(f"*** VIP LEVEL {self.vip_level} PRIORITY ***")
        super().book_session(session_name, *extras, **details)


vip = VIPMember("Zainab", "Gold")
vip.book_session("Yoga", "Towel", "Smoothie", time="6:00 PM", room="Studio A")