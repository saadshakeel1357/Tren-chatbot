from typing import Any, Text, Dict, List, Union, Optional
from rasa_sdk.events import UserUtteranceReverted
from rasa_sdk import Action, Tracker
from rasa_sdk.events import Restarted
from rasa_sdk.events import ActionExecutionRejected
from rasa_sdk.executor import CollectingDispatcher
import pandas as pd
from rasa_sdk.events import SlotSet

# Read the movie data from a CSV file
df = pd.read_csv("tmdb_5000_movies.csv")

# List of valid genres
valid_genres = ["action", "comedy", "thriller", "family", "adventure", "drama", "horror", "romance", "animation", "children", "fantasy", "crime", "mystery", "sci fi", "scifi", "sci-fi", "western", "documentary", "war", "musical"]

class DisplayGenres(Action):
    def name(self) -> Text:
        return "action_display_genres"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Union[Text, Dict[Text, Any]]]]:
        # Retrieve the selected genres from the conversation tracker
        init_genres = tracker.get_slot('genres')
        genres = []

        # Filter out invalid genres and convert them to lowercase
        for i in range(len(init_genres)):
            if init_genres[i].lower() in valid_genres:
                genres.append(init_genres[i].lower())

        # Check if any genres are selected
        if genres:
            # Generate a message with the selected genres
            dispatcher.utter_message(f"The genres you selected are: {', '.join([genre.title() for genre in genres])}")
        else:
            dispatcher.utter_message("You have not selected any genres yet.")

        return []

class SearchMovie(Action):
    def name(self) -> Text:
        return "action_search_movie"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Union[Text, Dict[Text, Any]]]]:
        # Retrieve the selected genres from the conversation tracker
        init_genres = tracker.get_slot('genres')
        genres = []

        # Filter out invalid genres and convert them to lowercase
        for i in range(len(init_genres)):
            if init_genres[i].lower() in valid_genres:
                genres.append(init_genres[i].lower())

        # Check the number of selected genres and apply filters accordingly
        if len(genres) == 1:
            mask = df['genres'].str.contains(genres[0].title())
        elif len(genres) == 2:
            mask = df['genres'].str.contains(genres[0].title()) & df['genres'].str.contains(genres[1].title())
        elif len(genres) == 3:
            mask = df['genres'].str.contains(genres[0].title()) & df['genres'].str.contains(genres[1].title()) & df['genres'].str.contains(genres[2].title())
        elif len(genres) > 3:
            dispatcher.utter_message("More than 3 genres selected!")
        else:
            dispatcher.utter_message("NO genre specified")

        # Finding the best movie based on the selected genres
        try:
            search_result1 = df[mask].sort_values(by='popularity', ascending=False).iloc[0]
            dispatcher.utter_message("There you go")
            dispatcher.utter_message(f"Name: {search_result1['original_title']}\n"
                                     f"{search_result1['vote_count']} people rated this movie\n"
                                     f"Average rating: {search_result1['vote_average']}\n"
                                     f"Runtime: {search_result1['runtime']} minutes\n"
                                     f"Release date: {search_result1['release_date']}\n"
                                     f"Tagline: {search_result1['tagline']}\n"
                                     f"Overview: {search_result1['overview']}\n"
                                     f"Link to homepage: {search_result1['homepage']}\n")
        except:
            dispatcher.utter_message("Could not find the best movie with the current selection of genres. Please try again.\n")

        return []

class ActionRestart(Action):
    def name(self) -> Text:
        return "action_restart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Conversation restarted")

        # Reset the conversation tracker to its initial state
        return [Restarted()]

class ActionDefaultFallback(Action):
    def name(self):
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="I am having difficulty understanding you. Can you please rephrase your message?")

