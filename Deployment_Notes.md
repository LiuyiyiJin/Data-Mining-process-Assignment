# Deployment notes

## CRISP-DM

Run weekly batch scoring for active customers. Send a ranked list to a retention team. Monitor feature drift, score drift, calibration, recall after labels mature, outreach rate, and group-level performance. Retrain when drift or recall thresholds are breached.

## KDD

Use a review queue rather than automatic account action. Monitor precision at the analyst-capacity threshold, recall, alert volume, label delay, and temporal drift. Validate with time-based splits before production.

## SEMMA

Refresh segments on a documented cadence and compare cluster stability across seeds and time windows. Treat campaign recommendations as experiments; measure incremental outcomes rather than assuming clusters cause behavior.
