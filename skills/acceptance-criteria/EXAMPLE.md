# Example: acceptance-criteria

> Real output from Claude Code (Claude Opus 5.5), run on 2026-09-23 with this skill installed. The output is unedited. The scenario is fictional.
> The prompt doesn't name the skill: Claude recognized the situation and used it on its own.

## Prompt

```text
Engineering starts next week and I need to define "done" for this story.
User story: "As a freelancer, I want to set an invoice to repeat every month so that I don't have to recreate it each time."
Notes: the user picks a start date and an optional end date; each generated invoice gets the next sequential invoice number (legal requirement in France); the invoice is emailed automatically to the client on the scheduled date; the user can pause or stop the recurrence at any time.
```

## Output

Below are the acceptance criteria. Your notes left a few decisions open, so I picked a default for each and marked it **[Assumption]**. Confirm or change those before engineering starts, because each one changes what gets built and tested.

---

## Acceptance criteria: Monthly recurring invoice

**Terms used below**
- **Template:** the invoice the user sets to repeat. It holds the client, line items, amounts, VAT and payment terms.
- **Occurrence:** one invoice generated from the template.
- **Scheduled date:** the day an occurrence is due to be issued.
- **Send time:** 08:00 in the user's account timezone. **[Assumption]**

### Happy path

**HP1: Set up a recurrence**
Given a user is editing an invoice with a client who has a valid email address
When they turn on "Repeat monthly", choose start date 2026-10-05, leave the end date empty, and save
Then the invoice list shows the template as "Recurring · Active · Next: 5 Oct 2026 · No end date"
And no invoice number is assigned or sent at save time.

**HP2: An occurrence is generated on its date**
Given an active recurrence with start date 2026-10-05
When the scheduled job runs at 08:00 on 2026-10-05 in the account timezone
Then exactly one invoice is created with the template's client, line items, amounts and VAT
And its issue date is 2026-10-05
And its due date is the issue date plus the template's payment terms (for example, 30 days gives 2026-11-04)
And its status is "Sent".

**HP3: Sequential numbering (legal requirement in France)**
Given the highest invoice number issued in the account is F-2026-041
When an occurrence is generated
Then it gets F-2026-042
And no other invoice in the account, recurring or manual, has F-2026-042.

**HP4: Automatic email**
Given an occurrence was just generated
When generation finishes
Then an email goes to the client's email address within 15 minutes of the send time
And the email has the invoice PDF attached, and the PDF shows the same number, date and amounts as the invoice record
And the invoice's activity log shows "Emailed to <address> at <timestamp>".

**HP5: Later months**
Given an active recurrence with start date 2026-10-05
When each month's scheduled job runs
Then occurrences are created on 2026-11-05, 2026-12-05 and 2027-01-05, one per month.

**HP6: End date**
Given an active recurrence with start date 2026-10-05 and end date 2027-01-05
When 2027-01-05 is processed
Then the 2027-01-05 occurrence is generated, because the end date is inclusive **[Assumption]**
And the recurrence status changes to "Ended"
And no occurrence is generated on 2027-02-05.

**HP7: Pause**
Given an active recurrence whose next scheduled date is 2026-12-05
When the user clicks Pause on 2026-11-20
Then the status shows "Paused"
And no invoice is generated or emailed on 2026-12-05.

**HP8: Resume**
Given a recurrence that was paused on 2026-11-20
When the user clicks Resume on 2026-12-15
Then the next scheduled date is 2027-01-05
And no invoice is generated for the 2026-12-05 date that was skipped. Missed months are not backfilled. **[Assumption]**

**HP9: Stop**
Given an active or paused recurrence
When the user clicks Stop and confirms the dialog
Then the status shows "Stopped" and no further occurrences are generated
And there is no Resume option. Stop is permanent, and to start again the user creates a new recurrence. **[Assumption]**
And invoices already generated keep their numbers, statuses and PDFs.

**HP10: Editing the template**
Given an active recurrence that has already generated 2 occurrences
When the user changes a line item's price on the template and saves
Then the next occurrence uses the new price
And the 2 invoices already generated do not change.

### Error states

**E1: Client has no email address**
Given the selected client has no email address
When the user tries to turn on "Repeat monthly"
Then saving is blocked with the message "Add an email address for this client to send recurring invoices."

**E2: End date before start date**
Given a start date of 2026-10-05
When the user enters an end date of 2026-09-30 and saves
Then saving is blocked with an inline error on the end date field.

**E3: Start date in the past**
Given today is 2026-09-23
When the user picks a start date of 2026-09-01
Then the date picker does not accept it and shows "Start date must be today or later."
And no invoice is generated for past dates.

**E4: Email bounce or delivery failure**
Given an occurrence was generated
When the email provider reports a bounce or a failure that cannot be retried
Then the invoice status is "Send failed"
And the user gets an in-app notification and an email naming the invoice number and the reason
And the invoice keeps its number. It is not deleted or renumbered, because French law does not allow gaps in the sequence.
And the user can click "Resend" from the invoice.

**E5: Email provider temporarily unavailable**
Given the email provider returns a temporary error
When sending is attempted
Then it is retried at least 3 times over 1 hour
And if it still fails, E4 applies.

**E6: Generation fails**
Given invoice creation fails partway through, for example because the database write fails
When the job finishes
Then no invoice number is used up. The next successful invoice takes the next unused number, and the sequence has no gaps.
And the job retries that occurrence within the same day
And if it has still failed by 23:59 on the scheduled date, the user is notified.

**E7: Client deleted or archived**
Given an active recurrence whose client has been archived
When the next scheduled date arrives
Then no invoice is generated
And the recurrence is automatically paused
And the user is notified: "Recurring invoice paused: client <name> is archived."

### Edge cases

**EC1: Start date on the 29th to 31st**
Given a start date of 2027-01-31
When February is processed
Then the occurrence is generated on 2027-02-28, the last day of the month
And the March occurrence is generated on 2027-03-31. The schedule goes back to the original day and does not stay on the 28th.

**EC2: A manual invoice and an occurrence created at the same moment**
Given the user creates a manual invoice at the same second the recurring job generates an occurrence
When both are saved
Then they get two different consecutive numbers
And the invoice issued later never has a lower number than one issued earlier.

**EC3: The job runs twice**
Given the scheduler fires twice for the same recurrence and the same scheduled date, for example after a retry or crash recovery
When both runs execute
Then exactly one invoice exists for that date and exactly one email is sent.

**EC4: Pausing on the scheduled date**
Given a recurrence scheduled for 2026-12-05 at 08:00
When the user pauses at 07:59 on 2026-12-05
Then no invoice is generated that day
And if they pause at 08:01, after generation, the generated invoice stands and pausing affects only future dates.

**EC5: Timezone and daylight saving time**
Given the account timezone is Europe/Paris
When the scheduled date falls on a daylight saving change (for example 2027-03-28)
Then the invoice is generated once, at 08:00 Paris time, with issue date 2027-03-28.

**EC6: Client email changed between occurrences**
Given the client's email is changed after the first occurrence
When the next occurrence is sent
Then it goes to the new address.

**EC7: A generated invoice is voided**
Given an occurrence F-2026-042 was generated
When the user tries to delete it
Then deletion is not possible. The only way to cancel it is a credit note, which is outside this story.
And the recurrence is not affected.

**EC8: End date equals start date**
Given the start date and end date are both 2026-10-05
When saving
Then saving is allowed, exactly one invoice is generated, and the status then shows "Ended".

**EC9: Numbering across a year boundary**
Given the number format includes the year
When the first occurrence of 2027 is generated
Then the numbering follows the account's existing yearly reset rule, the same way it does for manual invoices, and recurring invoices do not get a separate counter.

### Out of scope
- Frequencies other than monthly: weekly, quarterly, yearly or custom
- Generating an occurrence as a draft for the user to review before it is sent
- Backfilling months that were missed while paused
- Automatic payment or card charging
- Automatic credit notes or voiding
- Setting a different email subject or body for each occurrence (the existing invoice email template is used)
- Payment reminders or dunning for unpaid recurring invoices
- Pro-rating a partial first or last month
- Changing the start date of an active recurrence (the user stops it and creates a new one)

---

### Decisions to confirm
1. **Send time.** Is 08:00 in the account timezone right, or should the user choose the time?
2. **Pause or resume.** Should missed months be skipped (as assumed here) or backfilled?
3. **Stop.** Should it be permanent (as assumed here), or just a pause with no resume date?
4. **Review before sending.** Some freelancers bill variable hours and will want to check each invoice before it goes out. If that's common among your users, this story as written won't help them, and a draft-first option is the missing piece.
5. **Sequential numbering.** Check EC2, EC3 and E6 with whoever owns compliance. Most real bugs with the French numbering rule come from invoices created at the same moment and from failed generations.

I kept this in chat. I can put it in a shareable doc or a Notion page if that's easier for the team.
