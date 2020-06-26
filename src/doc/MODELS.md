Model Architecture planning

Membership (never change)
    -slug: for the long run, it is easier to use slug rather than ID in URL, for better naming
    -type                          (free, pro, enterprise)
    -price
    -stripe plan id


UserMembership
    -user                       (foreignkey to default user)
    -stripe customer id
    -membership type            (foreignkey to Membership)


Subscription
    -user membership            (foreignkey to UserMembership)
    -stripe subscription id     
    -active


Course
    -slug
    -title
    -description
    -allow memberships          (ManyToManyField to Membership)


Lesson
    -slug
    -title
    -course                     (foreignkey to Course)
    -position
    -video
    -thumbnail