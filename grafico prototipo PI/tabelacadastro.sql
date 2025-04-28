create table cadastro(
	id integer auto_increment primary key not null unique,
    consumo float not null,
    nr float not null,
    energia float not null,
    trans varchar(30) not null
    )
    
#select * from cadastro;