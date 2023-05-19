import time
import csv
import os

while True:
    # Check if there are any available GPUs
    gpu_ids = os.popen('nvidia-smi --query-gpu=index --format=csv,noheader').read().strip().split('\n')
    free_gpus = []
    for gpu_id in gpu_ids:
        gpu_info = os.popen(f'nvidia-smi -i {gpu_id} --query-gpu=memory.free --format=csv,noheader,nounits').read().strip()
        if int(gpu_info) > 10000:  # Check if GPU has at least 10GB of free memory
            free_gpus.append(gpu_id)
    
    # Check if there are any models to train
    with open('models.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip header
        for row in reader:
            model_id, model_name, backbone, learning_rate, epochs, batch_size = row
            
            # If there are free GPUs and the model has not been trained yet
            if free_gpus and os.path.exists(f'{model_name}.h5') == False:
                gpu_id = free_gpus.pop(0)
                
                # Set CUDA_VISIBLE_DEVICES to the ID of the selected GPU
                os.environ['CUDA_VISIBLE_DEVICES'] = gpu_id
                
                # Write the sbatch script
                with open(f'{model_name}.sbatch', 'w') as sbatch_file:
                    sbatch_file.write(f'''#!/bin/bash
#SBATCH --job-name={model_name}
#SBATCH --output={model_name}.out
#SBATCH --error={model_name}.err
#SBATCH --gres=gpu:1
#SBATCH --mem=32G
#SBATCH --time=24:00:00
#SBATCH --cpus-per-task=4

module load anaconda3
source activate my_env

python train_model.py --model_name {model_name} --backbone {backbone} --learning_rate {learning_rate} --epochs {epochs} --batch_size {batch_size}''')
                
                # Start the sbatch job and remove the model from the CSV file
                os.system(f'sbatch {model_name}.sbatch')
                time.sleep(10)  # Wait for the job to start
                os.system(f'sed -i "/^{model_id}/d" models.csv')
                
    time.sleep(300)  # Check for available GPUs and models every 5 minutes
