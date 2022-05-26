class GameStats():
    """Track stats for the game."""

    def __init__(self, ai_settings):
        """Initialize stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start game in an active state
        self.game_active = True

    def reset_stats(self):
        """Initialize stats that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit