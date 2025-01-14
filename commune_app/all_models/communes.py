from django.db import models


def validate_wallet(wallet):
    if (wallet < 0):
        raise Exception("negative wallet balance")


class Commune(models.Model):
    """
    The commune object stores the following:
    Name
    Description of the commune
    Wallet balance
    """
    name = models.CharField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=250, blank=True)
    wallet = models.IntegerField(default=0, validators=[validate_wallet])

    def clean(self) -> None:
        validate_wallet(self.wallet)
        return super().clean()

    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

    def wallet_charge(self, budget):
        '''
        set wallet balance:
        To make a charge that will be deducted from the balance enter a positive,
        Enter a negative number for the wallet credit.
        '''
        if (self.wallet < budget):
            raise Exception("will enter negative balance")
        else:
            self.wallet -= budget
