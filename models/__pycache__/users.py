o
    F??c?  ?                   @   s"   d dl mZ G dd? dej?ZdS )?    )?dbc                   @   sh   e Zd ZdZejejdd?Zeje?? ddd?Z	eje?? dd?Z
eje?? dd?Zejdd	d
d?ZdS )?User?USERST)?primary_keyF)?nullable?unique)r   )?default?Card?userzall, delete)?backref?cascadeN)?__name__?
__module__?__qualname__?__tablename__r   ?Column?Integer?id?String?email?password?Boolean?admin?relationship?cards? r   r   ?9/home/karla/flask-practice/trello_project/models/users.pyr      s    
?r   N)?mainr   ?Modelr   r   r   r   r   ?<module>   s    