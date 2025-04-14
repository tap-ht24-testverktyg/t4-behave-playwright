# Som en användare vill jag dölja rutan
# för att lägga till fler spelare när vi är igång,
# så att jag inte blir distraherad.

Feature: Dölja formuläret för att lägga till spelare

  Scenario: Dölja formuläret
    Given spelaren är på startsidan
    When spelaren klickar på knappen "Lägg till spelare"
    Then formuläret för att lägga till spelare visas
    And spelaren klickar på knappen "Dölj"
    Then formuläret för att lägga till spelare inte visas
