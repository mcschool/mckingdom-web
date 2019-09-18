use mckingdom;

CREATE TABLE migrate_version (
  repository_id VARCHAR(255),
  repository_path TEXT,
  version INT DEFAULT 0
);

INSERT INTO migrate_version (repository_id, repository_path, version) VALUES ('mckingdom', '', 0);
