import tkinter as tk
from tkinter import messagebox
from pygame import mixer
import json
import os


class MillionaireGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Wer wird Millionär")
        self.root.geometry("800x600")
        self.root.configure(bg="black")
