from runtime.presence import PresenceManager
from runtime.presence import PresenceState

presence = PresenceManager()

print(presence.state)

presence.set_state(
    PresenceState.LISTENING
)

print(presence.state)