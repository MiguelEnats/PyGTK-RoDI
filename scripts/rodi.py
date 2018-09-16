import requests, json  # fades.pypi

class RoDI(object):
    '''
    The RoDI (Robot Didactico Inalambrico) class
    '''
    _URL = 'http://{ip}:{port}/{method}/{args}'
    BLINK_METHOD = 1
    SENSE_METHOD = 2
    MOVE_METHOD = 3
    SING_METHOD = 4
    SEE_METHOD = 5
    PIXEL_METHOD = 6
    LIGHT_METHOD = 7
    LED_METHOD = 8

    def __init__(self, ip='192.168.4.1', port='1234'):
        '''
        Constructor for the robot
        '''
        self.robot_ip = ip
        self.port = port

    def _build_url(self, method, args):
        '''
        Helper method to construct the server url
        '''
        args = map(str, args)
        url = self._URL.format(
            ip=self.robot_ip,
            port=self.port,
            method=method,
            args='/'.join(args),
        )
        return url

    def blink(self, milliseconds):
        '''
        Makes the robot blink its led for the specified time
        '''
        url = self._build_url(
            self.BLINK_METHOD,
            [milliseconds]
        )
        requests.get(url)

    def move(self, left_wheel_speed, right_wheel_speed):
        '''
        Makes the robot move
        '''
        url = self._build_url(
            self.MOVE_METHOD,
            [left_wheel_speed, right_wheel_speed]
        )
        requests.get(url)

    def sing(self, note, duration):
        '''
        Makes the robot sing

        You need to specify a note and a duration in miliseconds
        (Notes can be found in http://arduino.cc/en/tutorial/tone)
        '''
        url = self._build_url(
            self.SING_METHOD,
            [note, duration]
        )
        requests.get(url)

    def see(self):
        '''
        Makes the robot "see"

        It returns the distance of an object in front of the robot in cm
        '''
        url = self._build_url(
            self.SEE_METHOD,
            []
        )
        response = requests.get(url)
        return json.loads(response.content)

    def sense(self):
        '''
        Senses the status of the infrarred sensors (line follower)

        Returns the reflectance of the object beneath the robot
        with values from 0 (black) to 1023 (white)
        '''
        url = self._build_url(
            self.SENSE_METHOD,
            []
        )
        response = requests.get(url)
        return json.loads(response.content)

    def pixel(self, red, green, blue):
        '''
        Changes the color of the Pixel in the robot

        Takes thre values, red, green and blue from 0 to 255
        '''
        url = self._build_url(
            self.PIXEL_METHOD,
            [red, green, blue]
        )
        requests.get(url)

    def light(self):
        '''
        Senses the status of the light sensors

        Returns the luminosity of the ambient with values from 0 to 1023
        '''
        url = self._build_url(
            self.LIGHT_METHOD,
            []
        )
        response = requests.get(url)
        return json.loads(response.content)

    def led(self, state):
        '''
        Turns the led on or off

        values for state are 0: off and 1: on
        '''
        url = self._build_url(
            self.LED_METHOD,
            [state]
        )
        requests.get(url)