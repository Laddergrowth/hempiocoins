def add_subscription_hccoins(hccoins, previous_plan, plan, cancelled_on):
    """
    Add an amount of hccoins to an existing coin value.

    :param hccoins: Existing coin value
    :type hccoins: int
    :param previous_plan: Previous subscription plan
    :type previous_plan: dict
    :param plan: New subscription plan
    :type plan: dict
    :param cancelled_on: When a plan has potentially been cancelled
    :type cancelled_on: datetime
    :return: int
    """
    # Some people will try to game the system and cheat us for extra hccoins.
    #
    # Users should only be able to gain hccoins via subscription when:
    #   Subscribes for the first time
    #   Subscriber updates to a better plan (one with more hccoins)
    #
    # That means the following actions should result in no hccoins:
    #   Subscriber cancels and signs up for the same plan
    #   Subscriber downgrades to a worse plan
    #
    # This method is still cheatable by signing up for a free trial on a plan,
    # and then upgrading to a higher plan. However, only a small amount of
    # users will do this, and once their subscription runs out they will be
    # removed from the leaderboard.
    #
    # I feel like it's better to allow them to temporarily cheat the system
    # instead of adding subscription hccoins during the invoicing phase which
    # will mean that honest people who subscribe won't be able to get their
    # hccoins until after the free trial period.
    previous_plan_hccoins = 0
    plan_hccoins = plan['metadata']['hccoins']

    if previous_plan:
        previous_plan_hccoins = previous_plan['metadata']['hccoins']

    if cancelled_on is None and plan_hccoins == previous_plan_hccoins:
        coin_adjustment = plan_hccoins
    elif plan_hccoins <= previous_plan_hccoins:
        return hccoins
    else:
        # We only want to add the difference between upgrading plans,
        # because they were already credited the previous plan's hccoins.
        coin_adjustment = plan_hccoins - previous_plan_hccoins

    return hccoins + coin_adjustment
