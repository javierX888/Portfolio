-- Migration script to add enhanced fields to Task table
-- Execute this in your Neon PostgreSQL console

-- Add new columns to task table
ALTER TABLE task ADD COLUMN IF NOT EXISTS priority INTEGER DEFAULT 2;
ALTER TABLE task ADD COLUMN IF NOT EXISTS status VARCHAR(20) DEFAULT 'pending';
ALTER TABLE task ADD COLUMN IF NOT EXISTS category VARCHAR(50) DEFAULT 'personal';
ALTER TABLE task ADD COLUMN IF NOT EXISTS start_date TIMESTAMP;
ALTER TABLE task ADD COLUMN IF NOT EXISTS due_date TIMESTAMP;
ALTER TABLE task ADD COLUMN IF NOT EXISTS completed_at TIMESTAMP;
ALTER TABLE task ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP;
ALTER TABLE task ADD COLUMN IF NOT EXISTS estimated_time INTEGER;
ALTER TABLE task ADD COLUMN IF NOT EXISTS is_recurring BOOLEAN DEFAULT FALSE;
ALTER TABLE task ADD COLUMN IF NOT EXISTS recurrence_pattern VARCHAR(20);
ALTER TABLE task ADD COLUMN IF NOT EXISTS recurrence_end_date TIMESTAMP;
ALTER TABLE task ADD COLUMN IF NOT EXISTS recurrence_days VARCHAR(50);

-- Update existing tasks to have default values
UPDATE task SET priority = 2 WHERE priority IS NULL;
UPDATE task SET status = 'pending' WHERE status IS NULL;
UPDATE task SET category = 'personal' WHERE category IS NULL;
UPDATE task SET is_recurring = FALSE WHERE is_recurring IS NULL;
UPDATE task SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL;

-- Update completed tasks to have completed status
UPDATE task SET status = 'completed' WHERE completed = TRUE AND status = 'pending';

-- Add indexes for better performance
CREATE INDEX IF NOT EXISTS idx_task_user_id ON task(user_id);
CREATE INDEX IF NOT EXISTS idx_task_due_date ON task(due_date);
CREATE INDEX IF NOT EXISTS idx_task_status ON task(status);
CREATE INDEX IF NOT EXISTS idx_task_priority ON task(priority);
CREATE INDEX IF NOT EXISTS idx_task_category ON task(category);

-- Verify the changes
SELECT column_name, data_type, column_default 
FROM information_schema.columns 
WHERE table_name = 'task' 
ORDER BY ordinal_position;
