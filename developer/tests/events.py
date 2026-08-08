from runtime.events import Event
from runtime.events import EventBus
from runtime.events import EventType


bus = EventBus()


def wake(event):

    print("WAKE:", event.payload)


bus.subscribe(

    EventType.WAKE,

    wake,

)

bus.publish(

    Event(

        EventType.WAKE,

        "Hey Friday",

    )

)