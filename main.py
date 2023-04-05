import models


ded: models.LiteraryCharacter = models.LiteraryCharacter("Максим", 95, "скверный, сварливый")
masha: models.LiteraryCharacter = models.LiteraryCharacter("Маша", 9, "весёлая, жизнерадостная, смешливая")
ludmila: models.LiteraryCharacter = models.LiteraryCharacter("Люда", 24, "замкнутая, скрытная, депрессивная")

ded.introduce()
masha.introduce()
ludmila.introduce()
