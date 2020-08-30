-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 30, 2020 at 12:42 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `molly`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add company insert', 1, 'add_companyinsert'),
(2, 'Can change company insert', 1, 'change_companyinsert'),
(3, 'Can delete company insert', 1, 'delete_companyinsert'),
(4, 'Can view company insert', 1, 'view_companyinsert'),
(5, 'Can add demo', 2, 'add_demo'),
(6, 'Can change demo', 2, 'change_demo'),
(7, 'Can delete demo', 2, 'delete_demo'),
(8, 'Can view demo', 2, 'view_demo'),
(9, 'Can add document', 3, 'add_document'),
(10, 'Can change document', 3, 'change_document'),
(11, 'Can delete document', 3, 'delete_document'),
(12, 'Can view document', 3, 'view_document'),
(13, 'Can add job insert', 4, 'add_jobinsert'),
(14, 'Can change job insert', 4, 'change_jobinsert'),
(15, 'Can delete job insert', 4, 'delete_jobinsert'),
(16, 'Can view job insert', 4, 'view_jobinsert'),
(17, 'Can add user insert', 5, 'add_userinsert'),
(18, 'Can change user insert', 5, 'change_userinsert'),
(19, 'Can delete user insert', 5, 'delete_userinsert'),
(20, 'Can view user insert', 5, 'view_userinsert'),
(21, 'Can add user resumes', 6, 'add_userresumes'),
(22, 'Can change user resumes', 6, 'change_userresumes'),
(23, 'Can delete user resumes', 6, 'delete_userresumes'),
(24, 'Can view user resumes', 6, 'view_userresumes'),
(25, 'Can add log entry', 7, 'add_logentry'),
(26, 'Can change log entry', 7, 'change_logentry'),
(27, 'Can delete log entry', 7, 'delete_logentry'),
(28, 'Can view log entry', 7, 'view_logentry'),
(29, 'Can add permission', 8, 'add_permission'),
(30, 'Can change permission', 8, 'change_permission'),
(31, 'Can delete permission', 8, 'delete_permission'),
(32, 'Can view permission', 8, 'view_permission'),
(33, 'Can add group', 9, 'add_group'),
(34, 'Can change group', 9, 'change_group'),
(35, 'Can delete group', 9, 'delete_group'),
(36, 'Can view group', 9, 'view_group'),
(37, 'Can add user', 10, 'add_user'),
(38, 'Can change user', 10, 'change_user'),
(39, 'Can delete user', 10, 'delete_user'),
(40, 'Can view user', 10, 'view_user'),
(41, 'Can add content type', 11, 'add_contenttype'),
(42, 'Can change content type', 11, 'change_contenttype'),
(43, 'Can delete content type', 11, 'delete_contenttype'),
(44, 'Can view content type', 11, 'view_contenttype'),
(45, 'Can add session', 12, 'add_session'),
(46, 'Can change session', 12, 'change_session'),
(47, 'Can delete session', 12, 'delete_session'),
(48, 'Can view session', 12, 'view_session'),
(49, 'Can add jobs', 13, 'add_jobs'),
(50, 'Can change jobs', 13, 'change_jobs'),
(51, 'Can delete jobs', 13, 'delete_jobs'),
(52, 'Can view jobs', 13, 'view_jobs'),
(53, 'Can add personality_insight', 14, 'add_personality_insight'),
(54, 'Can change personality_insight', 14, 'change_personality_insight'),
(55, 'Can delete personality_insight', 14, 'delete_personality_insight'),
(56, 'Can view personality_insight', 14, 'view_personality_insight');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'admin', 'logentry'),
(9, 'auth', 'group'),
(8, 'auth', 'permission'),
(10, 'auth', 'user'),
(11, 'contenttypes', 'contenttype'),
(1, 'recruiter', 'companyinsert'),
(2, 'recruiter', 'demo'),
(3, 'recruiter', 'document'),
(4, 'recruiter', 'jobinsert'),
(13, 'recruiter', 'jobs'),
(14, 'recruiter', 'personality_insight'),
(5, 'recruiter', 'userinsert'),
(6, 'recruiter', 'userresumes'),
(12, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2020-07-27 12:13:02.412603'),
(2, 'auth', '0001_initial', '2020-07-27 12:13:04.167214'),
(3, 'admin', '0001_initial', '2020-07-27 12:13:20.396881'),
(4, 'admin', '0002_logentry_remove_auto_add', '2020-07-27 12:13:25.104201'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2020-07-27 12:13:25.225875'),
(6, 'contenttypes', '0002_remove_content_type_name', '2020-07-27 12:13:26.682541'),
(7, 'auth', '0002_alter_permission_name_max_length', '2020-07-27 12:13:28.265542'),
(8, 'auth', '0003_alter_user_email_max_length', '2020-07-27 12:13:28.525509'),
(9, 'auth', '0004_alter_user_username_opts', '2020-07-27 12:13:28.622847'),
(10, 'auth', '0005_alter_user_last_login_null', '2020-07-27 12:13:30.087520'),
(11, 'auth', '0006_require_contenttypes_0002', '2020-07-27 12:13:30.142343'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2020-07-27 12:13:30.391680'),
(13, 'auth', '0008_alter_user_username_max_length', '2020-07-27 12:13:30.699742'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2020-07-27 12:13:30.943317'),
(15, 'auth', '0010_alter_group_name_max_length', '2020-07-27 12:13:31.256270'),
(16, 'auth', '0011_update_proxy_permissions', '2020-07-27 12:13:31.411277'),
(17, 'recruiter', '0001_initial', '2020-07-27 12:13:35.276742'),
(18, 'sessions', '0001_initial', '2020-07-27 12:13:37.000859'),
(19, 'recruiter', '0002_jobs', '2020-07-28 05:55:01.046074'),
(20, 'recruiter', '0002_auto_20200730_1653', '2020-07-30 11:23:36.998795');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `personality_insight`
--

CREATE TABLE `personality_insight` (
  `id` int(11) NOT NULL,
  `big5_openness` double NOT NULL,
  `big5_conscientiousness` double NOT NULL,
  `big5_Extraversion` double NOT NULL,
  `big5_Agreeableness` double NOT NULL,
  `big5_Emotional_range` double NOT NULL,
  `needs_Challenge` double NOT NULL,
  `needs_Closeness` double NOT NULL,
  `needs_Curiosity` double NOT NULL,
  `needs_Excitement` double NOT NULL,
  `needs_Harmony` double NOT NULL,
  `needs_Ideal` double NOT NULL,
  `needs_Liberty` double NOT NULL,
  `needs_Love` double NOT NULL,
  `needs_Practicality` double NOT NULL,
  `needs_Self_expression` double NOT NULL,
  `needs_Stability` double NOT NULL,
  `values_Openness_to_change` double NOT NULL,
  `values_Conservation` double NOT NULL,
  `values_Hedonism` double NOT NULL,
  `values_Self_enhancement` double NOT NULL,
  `values_Self_transcendence` double NOT NULL,
  `avg` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `recruiter_companyinsert`
--

CREATE TABLE `recruiter_companyinsert` (
  `id` int(11) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone_number` varchar(11) NOT NULL,
  `company_name` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recruiter_companyinsert`
--

INSERT INTO `recruiter_companyinsert` (`id`, `first_name`, `last_name`, `email`, `phone_number`, `company_name`, `designation`, `password`) VALUES
(8, 'raj', 'r', 'raj@gmail.com', '1234567834', 'raju', 'hr', 'raj'),
(9, 'raju', 'sdfaf', 'safasdf@gmail.com', 'afafafasf', 'asfaf', 'asfasf', '12345'),
(10, 'safdas', 'adfadf', 'asfas@gmail.com', 'sdggggdsds', 'afsadgfgg', 'asfafadf', '12345');

-- --------------------------------------------------------

--
-- Table structure for table `recruiter_demo`
--

CREATE TABLE `recruiter_demo` (
  `id` int(11) NOT NULL,
  `full_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `mobile_number` varchar(11) NOT NULL,
  `message` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `recruiter_document`
--

CREATE TABLE `recruiter_document` (
  `id` int(11) NOT NULL,
  `document` varchar(100) NOT NULL,
  `uploaded_at` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `recruiter_jobinsert`
--

CREATE TABLE `recruiter_jobinsert` (
  `id` int(11) NOT NULL,
  `job_title` varchar(30) NOT NULL,
  `company_name` varchar(50) NOT NULL,
  `job_type` varchar(50) NOT NULL,
  `location` varchar(100) NOT NULL,
  `job_description` longtext NOT NULL,
  `qualifications` longtext NOT NULL,
  `additional_info` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recruiter_jobinsert`
--

INSERT INTO `recruiter_jobinsert` (`id`, `job_title`, `company_name`, `job_type`, `location`, `job_description`, `qualifications`, `additional_info`) VALUES
(5, 'Developer', 'facebook', 'full time', 'navsari', 'afaf', 'dfwsdef', 'afaqsfd'),
(6, 'Accountant', 'raju', 'fulltime', 'mumbai', 'wergfwreg', 'wefwef', 'wefgf'),
(7, 'Software Engineer', 'google', 'half time', 'london', 'gwrgrweg', 'gerg', 'wegwerg'),
(8, 'Clerk', 'flipkart', 'fulltime', 'ranchi', 'alhdfh', 'sghoosw', 'nsdgj'),
(9, 'Accountant', 'alupuri', 'fulltime', 'matunga', 'afhkf', 'hskadfdahf', 'hsdhfkdh'),
(10, 'Software Engineer', 'facebook', 'fulltime', 'amerika', 'sdgswdg', 'sfgwsg', 'fsgwsg'),
(11, 'Accountant', 'afadf', 'sdfgsdf', 'asdfadf', 'sadfadfad', 'adff', 'erdgf');

-- --------------------------------------------------------

--
-- Table structure for table `recruiter_jobs`
--

CREATE TABLE `recruiter_jobs` (
  `id` int(11) NOT NULL,
  `job_title` varchar(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `recruiter_jobs`
--

INSERT INTO `recruiter_jobs` (`id`, `job_title`) VALUES
(1, 'HR'),
(2, 'Accountant'),
(3, 'Clerk'),
(5, 'Software Engineer'),
(6, 'Developer');

-- --------------------------------------------------------

--
-- Table structure for table `resumeparser`
--

CREATE TABLE `resumeparser` (
  `Resume_ID` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `mobile` varchar(11) NOT NULL,
  `email` varchar(50) NOT NULL,
  `skills` varchar(500) NOT NULL,
  `company` varchar(500) DEFAULT NULL,
  `experience` longtext DEFAULT NULL,
  `experience_in_year` varchar(5) DEFAULT NULL,
  `designation` longtext DEFAULT NULL,
  `college_name` varchar(500) DEFAULT NULL,
  `degree` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `id` int(11) NOT NULL,
  `FirstName` varchar(100) NOT NULL,
  `LastName` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `PhoneNumber` varchar(11) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `document` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `personality_insight`
--
ALTER TABLE `personality_insight`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recruiter_companyinsert`
--
ALTER TABLE `recruiter_companyinsert`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recruiter_demo`
--
ALTER TABLE `recruiter_demo`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recruiter_document`
--
ALTER TABLE `recruiter_document`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recruiter_jobinsert`
--
ALTER TABLE `recruiter_jobinsert`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `recruiter_jobs`
--
ALTER TABLE `recruiter_jobs`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `resumeparser`
--
ALTER TABLE `resumeparser`
  ADD PRIMARY KEY (`Resume_ID`);

--
-- Indexes for table `user_info`
--
ALTER TABLE `user_info`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=57;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `personality_insight`
--
ALTER TABLE `personality_insight`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `recruiter_companyinsert`
--
ALTER TABLE `recruiter_companyinsert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `recruiter_demo`
--
ALTER TABLE `recruiter_demo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `recruiter_document`
--
ALTER TABLE `recruiter_document`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `recruiter_jobinsert`
--
ALTER TABLE `recruiter_jobinsert`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `recruiter_jobs`
--
ALTER TABLE `recruiter_jobs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `resumeparser`
--
ALTER TABLE `resumeparser`
  MODIFY `Resume_ID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `user_info`
--
ALTER TABLE `user_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
