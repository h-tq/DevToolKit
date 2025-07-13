import torch.nn as nn


def calculate_model_memory_size(model: nn.Module):
    total_param_size = 0
    total_param_count = 0

    for parameter in model.parameters():
        total_param_size += parameter.nelement() * parameter.element_size()
        total_param_count += parameter.nelement()

    total_buffer_size = 0
    total_buffer_count = 0

    for buffer in model.buffers():
        total_buffer_size += buffer.nelement() * buffer.element_size()
        total_buffer_count += buffer.nelement()

    total_size_mb = (total_param_size + total_buffer_size) / (1024 * 1024)
    print('Total model size: {:.3f} MB.'.format(total_size_mb))
    # print('The total_steps size of the model, including parameters and buffers, is {:.3f} MB.'.format(total_size_mb))

    return total_param_size, total_param_count, total_buffer_size, total_buffer_count, total_size_mb
