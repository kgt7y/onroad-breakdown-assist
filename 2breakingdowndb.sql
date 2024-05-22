-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Feb 13, 2024 at 07:49 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `2breakingdowndb`
--

-- --------------------------------------------------------

--
-- Table structure for table `booktb`
--

CREATE TABLE `booktb` (
  `id` int(10) NOT NULL auto_increment,
  `UserName` varchar(250) NOT NULL,
  `Umobile` varchar(250) NOT NULL,
  `VehicleType` varchar(250) NOT NULL,
  `VehicleNo` varchar(250) NOT NULL,
  `LandMark` varchar(500) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `FalutInfo` varchar(1000) NOT NULL,
  `Images` varchar(500) NOT NULL,
  `EmpName` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Status` varchar(250) NOT NULL,
  `Amount` varchar(250) NOT NULL,
  `Date` date NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `booktb`
--

INSERT INTO `booktb` (`id`, `UserName`, `Umobile`, `VehicleType`, `VehicleNo`, `LandMark`, `Address`, `FalutInfo`, `Images`, `EmpName`, `Mobile`, `Email`, `Status`, `Amount`, `Date`) VALUES
(1, 'san', 'sangeeth5535@gmail.com', 'TwoWheeler', '21BH2345AA', 'near pertrolbunk', 'no 6 trichy', 'break fail', '1556.png', 'san', '9486365535', 'sangeeth5535@gmail.com', 'Paid', '8000', '2024-01-11'),
(2, 'karthi', 'sangeeth5535@gmail.com', 'TwoWheeler', '21BH2345AA', 'near pertrolbunk', 'no 6 trichy', 'break nill', '6238.png', 'karthi', 'sangeeth5535@gmail.com', '9486365535', 'Paid', '800', '2024-02-13');

-- --------------------------------------------------------

--
-- Table structure for table `employeetb`
--

CREATE TABLE `employeetb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  `City` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=4 ;

--
-- Dumping data for table `employeetb`
--

INSERT INTO `employeetb` (`id`, `Name`, `Gender`, `Mobile`, `Email`, `Address`, `UserName`, `Password`, `City`) VALUES
(1, 'sangeeth Kumar', 'Male', '9486365535', 'sangeeth5535@gmail.com', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san', ''),
(2, 'karthi', 'Male', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'karthi', 'karthi', 'karthi'),
(3, 'karthi', 'Male', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'karthi', 'karthi', 'Trichy');

-- --------------------------------------------------------

--
-- Table structure for table `regtb`
--

CREATE TABLE `regtb` (
  `id` bigint(20) NOT NULL auto_increment,
  `Name` varchar(250) NOT NULL,
  `Gender` varchar(250) NOT NULL,
  `Mobile` varchar(250) NOT NULL,
  `Email` varchar(250) NOT NULL,
  `Address` varchar(500) NOT NULL,
  `UserName` varchar(250) NOT NULL,
  `Password` varchar(250) NOT NULL,
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;

--
-- Dumping data for table `regtb`
--

INSERT INTO `regtb` (`id`, `Name`, `Gender`, `Mobile`, `Email`, `Address`, `UserName`, `Password`) VALUES
(1, 'sangeeth Kumar', 'Male', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'san', 'san'),
(2, 'karthi', 'Male', 'sangeeth5535@gmail.com', '9486365535', 'No 16, Samnath Plaza, Madurai Main Road, Melapudhur', 'karthi', 'karthi');
