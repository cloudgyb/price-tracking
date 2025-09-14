 CREATE TABLE IF NOT EXISTS `goods` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(2000) NOT NULL DEFAULT '',
  `price` decimal(10,2) DEFAULT 0.00,
  `name` varchar(1000) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
 
 CREATE TABLE IF NOT EXISTS `goods_price` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `goods_id` bigint(20) unsigned NOT NULL,
  `price` decimal(10,2) NOT NULL DEFAULT 0.00,
  `create_time` datetime NOT NULL DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


