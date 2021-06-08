
--test query
--SELECT top 10 * FROM [tempdb].[sys].[columns]

/* Create database */
CREATE DATABASE Music;
GO

/* Change to the Music database */
USE Music;
GO

/* Create tables */
CREATE TABLE Artists (
    ArtistId int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    ArtistName nvarchar(255) NOT NULL,
    ActiveFrom DATE NULL
);

CREATE TABLE Genres (
    GenreId int IDENTITY(1,1) NOT NULL PRIMARY KEY,
    Genre nvarchar(50) NOT NULL
);

CREATE TABLE Albums
 (
  AlbumId int IDENTITY(1,1) NOT NULL PRIMARY KEY,
  AlbumName nvarchar(255) NOT NULL,
  ReleaseDate date NOT NULL,
  ArtistId int NOT NULL,
  GenreId int NOT NULL
  
  CONSTRAINT FK_Albums_Artists FOREIGN KEY (ArtistId)     
    REFERENCES dbo.Artists (ArtistId)     
    ON DELETE NO ACTION    
    ON UPDATE NO ACTION    
);
GO

USE [master];
DROP DATABASE Music;
DROP DATABASE vp;
