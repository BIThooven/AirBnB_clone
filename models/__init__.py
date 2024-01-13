#!/usr/bin/python3
"""creating storage instance"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
