from os import getenv

class Neha:
  THEMEE = getenv("THEMEE", "cerulean")
  AUTH_CHANNEL = getenv("AUTH_CHANNEL").split(", ")
