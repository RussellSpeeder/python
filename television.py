class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """Initialize the Television."""
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self) -> None:
        """Turns the TV on or off."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mutes or unmutes the TV."""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """Increases the TV channel."""
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """Decreases the TV channel."""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increases the TV volume by one."""
        if self.__status and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decreases the TV volume by one."""
        if self.__status and not self.__muted:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Returns string of the TV."""
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}" + (" (Muted)" if self.__muted else "")

