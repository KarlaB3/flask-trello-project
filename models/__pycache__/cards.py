o
    ��cz  �                   @   s"   d dl mZ G dd� dej�ZdS )�    )�dbc                   @   s~   e Zd ZdZejejdd�Ze�e�� �Z	e�e�� �Z
e�e�� �Ze�e�� �Ze�e�� �Zejeje�d�dd�ZdS )�Card�CARDST)�primary_keyzUSERS.idF)�nullableN)�__name__�
__module__�__qualname__�__tablename__r   �Column�Integer�id�String�title�description�Date�date�status�priority�
ForeignKey�user_id� r   r   �9/home/karla/flask-practice/trello_project/models/cards.pyr      s    r   N)�mainr   �Modelr   r   r   r   r   �<module>   s    