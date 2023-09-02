import pytest
import datetime
from ohce import Ohce

app = Ohce()

def test_ohce():
  now = datetime.datetime.now().time()
  if now >= datetime.time(6) and now < datetime.time(12):
    assert app.ohce("ohce Sebastián") == "¡Buenas días Sebastián!"
  elif now >= datetime.time(12) and now < datetime.time(20):
    assert app.ohce("ohce Sebastián") == "¡Buenas tardes Sebastián!"
  else:
    assert app.ohce("ohce Sebastián") == "¡Buenas noches Sebastián!"

def test_palabra():
  assert app.ohce("ohce") == "echo"
  assert app.ohce("ohw") == "who"

def test_palindromo():
  assert app.ohce("oto") == "oto"+"\n"+"¡Bonita palabra!"

def test_Stop():
  assert app.ohce("Stop!") == "Adios Sebastián"