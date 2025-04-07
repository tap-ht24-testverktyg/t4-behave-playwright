# Som en användare vill jag lägga till namn på mig och min motspelare, så att vi kan ta tiden på våra drag.

Feature: Lägga till namn på spelare

  Scenario Outline: Lägga till två spelare
    Given spelaren är på startsidan
    When spelaren klickar på knappen "Lägg till spelare"
    And spelaren skriver "{David}" i textfältet
    And spelaren klickar på knappen "Lägg till spelare"
    Then "{David22}" dyker upp på sidan med texten "0:00.0"
    When spelaren skriver "{Gerson}" i textfältet
    And spelaren klickar på knappen "Lägg till spelare"
    Then "{Gerson}" dyker upp på sidan med texten "0:00.0"

    Examples:
    | user1 | user2  |
    | David | Gerson |
