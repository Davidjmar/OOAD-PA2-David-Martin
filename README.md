# OOAD-PA2-David-Martin
A late implementation of the PA2 coding assignment. Courtesy of unforgiving circumstances
This Project had an extension from Professor Montgomery to Sunday Oct. 6th
This may not have the cleanest implementatino but it was completed in only 2 days.

Contributor: David Martin

To run this program:
1. Open this project in VSCODE
2. Download the suggested plugins that popup on opening this file
3. Open AnnouncerAndKeeper.py
4. Click the green play button in the upper right corner OR  type: 
    /usr/local/opt/python/bin/python3.7  file's-path/OOAD-PA2-David-Martin/AnnouncerAndKeeper.py

**Observer Pattern**
The announcer is an instance of the subject which is maintained and updated by the conreteSubject class.
In this way, when the zookeeper is initialized and run, the concrete subject, the zookeeper will also initialize
    observable evenet for the subject, being the zoo announcer. On running the zookeeper signals updates to the zoo announcer via the .update() method. Then upon full completion the concrete subject(the zoo keeper) can detach the
    subject(zoo announcer) which will stop observing the events of the concrete subject and thus deconstruct from the method.

**Strategy Pattern**
Using the definition that "The strategy pattern allows you to change the implementation of something used at runtime."
    the most significant usages of the strategy pattern would be exisitng within the Animals.py file. In the class initializations the roambehavior is set at the species level, i.e. Pachyderm, Feline.. etc. But in cases of Elephant, Rhino, and Cat the implementation of the roamBehavior method is changed to another existing method at runtime. Essentially and override to a different existing method.

**References**
https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Observer.html
https://stackoverflow.com/questions/26422884/strategy-pattern-v-s-decorator-pattern
https://stackoverflow.com/questions/10860429/design-decision-factory-vs-observer-pattern
https://refactoring.guru/design-patterns/observer/python/example
https://stackoverflow.com/questions/39460671/python-getting-none-at-the-end-of-printing-a-list/39460685
