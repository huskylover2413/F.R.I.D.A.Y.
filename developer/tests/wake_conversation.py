from runtime.session import Session


session = Session()

session.initialize()

try:

    session.run()

except KeyboardInterrupt:

    session.shutdown()