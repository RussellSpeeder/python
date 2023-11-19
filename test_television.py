import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        """Test if the Television is initialized."""
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_power(self):
        """Test the power on/off."""
        self.tv.power()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'
        self.tv.power()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'

    def test_mute(self):
        """Test muting and unmuting."""
        self.tv.mute()
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0' 
        self.tv.power()
        self.tv.mute()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0 (Muted)'  

    def test_channel_up(self):
        """Test increasing the channel."""
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == 'Power = True, Channel = 1, Volume = 0'
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'

    def test_channel_down(self):
        """Test decreasing the channel."""
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == 'Power = True, Channel = 3, Volume = 0'
        self.tv.channel_down()
        self.tv.channel_down()
        self.tv.channel_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'

    def test_volume_up(self):
        """Test increasing the volume."""
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 1'
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_up()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 2'

    def test_volume_down(self):
        """Test decreasing the volume."""
        assert str(self.tv) == 'Power = False, Channel = 0, Volume = 0'
        self.tv.power()
        self.tv.volume_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'
        self.tv.volume_down()
        assert str(self.tv) == 'Power = True, Channel = 0, Volume = 0'

