


select * from app.auth_permission ap ;

select * from app.auth_group_permissions agp ;

select * from app.django_session ds ;
select * from app.app_role ar ; 
select * from app.auth_user au ;			--> User --> auth_user
select * from app.app_profile ap ;			--> User --> Prifile
select * from app.auth_group ag ;
select * from app.auth_user_groups aug ;	--	User --> groups
select * from app ;

delete from app.auth_user where username in('test_user','anower');


--insert into app.auth_user(password, username,first_name , last_name ,email, is_superuser, is_active, is_staff,date_joined) values 
--('12345','test_user','test_user','test_user', 'test_user@gmail.com',false, false, true,now());














