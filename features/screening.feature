Feature: hire or not to hire
  In order to reduce specialist workload on job interviews without sacrificing quality,
  I want to schedule additional interviews automatically based on experience of candidates and HR managers

  @weakBoth
  Scenario: Weak candidate and unexperienced HR and proceed
    Given the candidate has an experience of 0.5 year and HR manager has an experience of 0.4 year
     When scanned by HR manager and decided to proceed
     Then next interview round is ExtraRound
  @weakBoth
  Scenario: Weak candidate and unexperienced HR and notProceed
    Given the candidate has an experience of 0.5 year and HR manager has an experience of 0.4 year
     When scanned by HR manager and decided to notProceed
     Then next interview round is NoExtraRound


  @weakHR
  Scenario: Strong candidate and unexperienced HR and proceed
    Given the candidate has an experience of 1.5 year and HR manager has an experience of 0.4 year
     When scanned by HR manager and decided to proceed
     Then next interview round is ExtraRound

  @weakHR
  Scenario: Strong candidate and unexperienced HR and notProceed
    Given the candidate has an experience of 1.5 year and HR manager has an experience of 0.4 year
     When scanned by HR manager and decided to notProceed
     Then next interview round is ExtraRound


  @strongBoth
  Scenario: Strong candidate and experienced HR and proceed
    Given the candidate has an experience of 2.5 year and HR manager has an experience of 2.4 year
     When scanned by HR manager and decided to proceed
     Then next interview round is ExtraRound

  @strongBoth
  Scenario: Strong candidate and experienced HR and notProceed
    Given the candidate has an experience of 2.5 year and HR manager has an experience of 2.4 year
     When scanned by HR manager and decided to notProceed
     Then next interview round is NoExtraRound


  @weakCandidate
  Scenario: Unexperienced candidate and experienced HR and proceed
    Given the candidate has an experience of 0.5 year and HR manager has an experience of 2.4 year
     When scanned by HR manager and decided to proceed
     Then next interview round is ExtraRound

  @weakCandidate
  Scenario: Unexperienced candidate and experienced HR and notProceed
    Given the candidate has an experience of 0.5 year and HR manager has an experience of 2.4 year
     When scanned by HR manager and decided to notProceed
     Then next interview round is NoExtraRound

   


 