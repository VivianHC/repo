/*==============================================================*/
/* Table: course_info                                           */
/*==============================================================*/
create table course_info
(
   cid                  char(20) not null,
   c_name               char(50) not null,
   introduce            char(255) not null,
   primary key (cid)
);

alter table course_info comment '所有课程的基本信息表';

create table classes_info
(
   class_code           char(10) not null,
   tid                  char(10) not null,
   class_name           char(20) not null,
   class_grade          int not null,
   class_no             int not null,
   primary key (class_code)
);


create table teacher_course
(
   tid                  char(10) not null,
   cid                  char(20) not null,
   primary key (tid, cid)
);
